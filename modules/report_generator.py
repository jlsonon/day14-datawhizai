from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
import re

class ReportGenerator:
    @staticmethod
    def _parse_markdown_to_html(markdown_text):
        """Convert markdown to HTML for ReportLab Paragraph"""
        html = markdown_text
        
        # First escape HTML special characters (but preserve content)
        # We'll do this more carefully
        lines = html.split('\n')
        processed_lines = []
        
        for line in lines:
            # Skip separator lines
            if re.match(r'^[=\-]+$', line.strip()):
                continue
            
            # Convert headers first (before escaping)
            if line.strip().startswith('###'):
                line = re.sub(r'^###\s+(.+?)$', r'<b><font size="14">\1</font></b>', line.strip())
            elif line.strip().startswith('##'):
                line = re.sub(r'^##\s+(.+?)$', r'<b><font size="16">\1</font></b>', line.strip())
            elif line.strip().startswith('#'):
                line = re.sub(r'^#\s+(.+?)$', r'<b><font size="18">\1</font></b>', line.strip())
            else:
                # Convert bold **text** to <b>text</b>
                line = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', line)
                
                # Convert bullet points * item to • item
                if re.match(r'^\*\s+', line.strip()):
                    line = re.sub(r'^\*\s+(.+?)$', r'• \1', line.strip(), flags=re.MULTILINE)
                elif re.match(r'^\d+\.\s+', line.strip()):
                    line = re.sub(r'^(\d+)\.\s+(.+?)$', r'\1. \2', line.strip(), flags=re.MULTILINE)
            
            # Escape remaining HTML special characters
            # But preserve our tags
            line = line.replace('&', '&amp;')
            # Temporarily replace our tags
            line = line.replace('<b>', '___BOLD_START___')
            line = line.replace('</b>', '___BOLD_END___')
            line = line.replace('<font size="14">', '___FONT14_START___')
            line = line.replace('<font size="16">', '___FONT16_START___')
            line = line.replace('<font size="18">', '___FONT18_START___')
            line = line.replace('</font>', '___FONT_END___')
            
            # Now escape < and >
            line = line.replace('<', '&lt;').replace('>', '&gt;')
            
            # Restore our tags
            line = line.replace('___BOLD_START___', '<b>')
            line = line.replace('___BOLD_END___', '</b>')
            line = line.replace('___FONT14_START___', '<font size="14">')
            line = line.replace('___FONT16_START___', '<font size="16">')
            line = line.replace('___FONT18_START___', '<font size="18">')
            line = line.replace('___FONT_END___', '</font>')
            
            processed_lines.append(line)
        
        return '\n'.join(processed_lines)
    
    @staticmethod
    def _parse_markdown_to_plain_text(markdown_text):
        """Convert markdown to plain formatted text"""
        lines = markdown_text.split('\n')
        processed_lines = []
        
        for line in lines:
            original_line = line
            
            # Skip separator lines (===, ---)
            if re.match(r'^[=\-]+$', line.strip()):
                continue
            
            # Remove markdown headers but keep text
            if line.strip().startswith('###'):
                line = re.sub(r'^###\s+(.+?)$', r'\1', line.strip())
            elif line.strip().startswith('##'):
                line = re.sub(r'^##\s+(.+?)$', r'\1', line.strip())
            elif line.strip().startswith('#'):
                line = re.sub(r'^#\s+(.+?)$', r'\1', line.strip())
            else:
                # Remove markdown bold but keep text
                line = re.sub(r'\*\*(.+?)\*\*', r'\1', line)
                
                # Convert bullet points * item to • item (handle both * and *   formats)
                if re.match(r'^\*\s+', line.strip()):
                    line = re.sub(r'^\*\s+(.+?)$', r'• \1', line.strip())
                elif re.match(r'^\d+\.\s+', line.strip()):
                    # Keep numbered lists as is, just clean up spacing
                    line = re.sub(r'^(\d+)\.\s+(.+?)$', r'\1. \2', line.strip())
            
            processed_lines.append(line)
        
        text = '\n'.join(processed_lines)
        
        # Clean up extra blank lines
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        return text.strip()
    
    @staticmethod
    def generate_pdf(file_path, content):
        """Generate a PDF report with proper formatting from markdown"""
        try:
            doc = SimpleDocTemplate(file_path, pagesize=letter,
                                   rightMargin=72, leftMargin=72,
                                   topMargin=72, bottomMargin=72)
            styles = getSampleStyleSheet()
            story = []
            
            # Convert markdown to HTML
            html_content = ReportGenerator._parse_markdown_to_html(content)
            
            # Split content into paragraphs
            paragraphs = html_content.split('\n')
            
            for para in paragraphs:
                para = para.strip()
                if para:
                    # Check if it's a header
                    if '<font size="18">' in para:
                        p = Paragraph(para, styles['Heading1'])
                        story.append(p)
                        story.append(Spacer(1, 0.3 * inch))
                    elif '<font size="16">' in para:
                        p = Paragraph(para, styles['Heading2'])
                        story.append(p)
                        story.append(Spacer(1, 0.25 * inch))
                    elif '<font size="14">' in para:
                        p = Paragraph(para, styles['Heading3'])
                        story.append(p)
                        story.append(Spacer(1, 0.2 * inch))
                    elif para.startswith('<b>') and para.endswith('</b>') and len(para) < 100:
                        # Bold paragraph (section headers like **Executive Summary**)
                        p = Paragraph(para, styles['Heading2'])
                        story.append(p)
                        story.append(Spacer(1, 0.2 * inch))
                    else:
                        # Regular paragraph
                        p = Paragraph(para, styles['Normal'])
                        story.append(p)
                        story.append(Spacer(1, 0.15 * inch))
                elif len(story) > 0:  # Add spacing for blank lines
                    story.append(Spacer(1, 0.1 * inch))
            
            doc.build(story)
        except Exception as e:
            # Fallback to simple canvas method with formatted text
            c = canvas.Canvas(file_path, pagesize=letter)
            text = c.beginText(50, 750)
            text.setFont("Helvetica", 10)
            
            # Convert markdown to plain text
            plain_text = ReportGenerator._parse_markdown_to_plain_text(content)
            
            # Handle multi-line content
            lines = plain_text.split('\n')
            y_position = 750
            for line in lines:
                if y_position < 50:  # New page if needed
                    c.drawText(text)
                    c.showPage()
                    text = c.beginText(50, 750)
                    text.setFont("Helvetica", 10)
                    y_position = 750
                
                # Handle bold text (simple approach)
                if line.strip().startswith('**') or any(char.isupper() for char in line[:20]):
                    text.setFont("Helvetica-Bold", 10)
                else:
                    text.setFont("Helvetica", 10)
                
                text.setTextOrigin(50, y_position)
                text.textLine(line[:90])  # Limit line length
                y_position -= 15
            
            c.drawText(text)
            c.save()
    
    @staticmethod
    def generate_markdown(file_path, content):
        """Generate a formatted text file (converted from markdown)"""
        # Convert markdown to plain formatted text
        formatted_text = ReportGenerator._parse_markdown_to_plain_text(content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(formatted_text)