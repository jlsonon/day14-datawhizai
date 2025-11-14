import pandas as pd
import numpy as np

class DataCalculator:
    """Helper class to perform calculations on dataframes and provide concrete answers"""
    
    def __init__(self, df):
        self.df = df
    
    def get_average_by_column(self, column_name):
        """Get average of a specific column"""
        if column_name in self.df.columns:
            return self.df[column_name].mean()
        return None
    
    def get_sum_by_column(self, column_name):
        """Get sum of a specific column"""
        if column_name in self.df.columns:
            return self.df[column_name].sum()
        return None
    
    def get_grouped_average(self, group_by_col, value_col):
        """Get average values grouped by a column"""
        if group_by_col in self.df.columns and value_col in self.df.columns:
            return self.df.groupby(group_by_col)[value_col].mean().to_dict()
        return None
    
    def get_yearly_average(self, year_col='Year', value_col='Value'):
        """Get average values by year"""
        if year_col in self.df.columns and value_col in self.df.columns:
            return self.df.groupby(year_col)[value_col].mean().to_dict()
        return None
    
    def filter_and_calculate(self, filters, calculation_col, calculation_type='mean'):
        """
        Filter dataframe and perform calculation
        filters: dict like {'Year': 2024, 'Industry': 'Manufacturing'}
        calculation_type: 'mean', 'sum', 'count', 'min', 'max'
        """
        filtered_df = self.df.copy()
        
        # Apply filters
        for col, value in filters.items():
            if col in filtered_df.columns:
                if isinstance(value, list):
                    filtered_df = filtered_df[filtered_df[col].isin(value)]
                else:
                    filtered_df = filtered_df[filtered_df[col] == value]
        
        # Perform calculation
        if calculation_col in filtered_df.columns:
            if calculation_type == 'mean':
                return filtered_df[calculation_col].mean()
            elif calculation_type == 'sum':
                return filtered_df[calculation_col].sum()
            elif calculation_type == 'count':
                return filtered_df[calculation_col].count()
            elif calculation_type == 'min':
                return filtered_df[calculation_col].min()
            elif calculation_type == 'max':
                return filtered_df[calculation_col].max()
        
        return None
    
    def get_summary_stats(self, column_name):
        """Get comprehensive statistics for a column"""
        if column_name in self.df.columns and pd.api.types.is_numeric_dtype(self.df[column_name]):
            return {
                'mean': self.df[column_name].mean(),
                'median': self.df[column_name].median(),
                'std': self.df[column_name].std(),
                'min': self.df[column_name].min(),
                'max': self.df[column_name].max(),
                'sum': self.df[column_name].sum(),
                'count': self.df[column_name].count()
            }
        return None
    
    def format_number(self, number, prefix='', suffix='', decimals=2):
        """Format number for display"""
        if number is None:
            return "N/A"
        
        if decimals == 0:
            return f"{prefix}{number:,.0f}{suffix}"
        else:
            return f"{prefix}{number:,.{decimals}f}{suffix}"
    
    def generate_answer_with_values(self, question, filters=None, calculation_col='Value'):
        """
        Generate a complete answer with actual calculated values
        """
        question_lower = question.lower()
        answer_parts = []
        
        # Detect what kind of question it is
        if 'average' in question_lower or 'mean' in question_lower:
            if filters:
                result = self.filter_and_calculate(filters, calculation_col, 'mean')
            else:
                result = self.get_average_by_column(calculation_col)
            
            if result is not None:
                answer_parts.append(f"**Average {calculation_col}:** {self.format_number(result, prefix='$', suffix=' million' if 'million' in str(self.df.columns) else '')}")
        
        if 'total' in question_lower or 'sum' in question_lower:
            if filters:
                result = self.filter_and_calculate(filters, calculation_col, 'sum')
            else:
                result = self.get_sum_by_column(calculation_col)
            
            if result is not None:
                answer_parts.append(f"**Total {calculation_col}:** {self.format_number(result, prefix='$', suffix=' million' if 'million' in str(self.df.columns) else '')}")
        
        if 'by year' in question_lower or 'over the years' in question_lower or 'from' in question_lower:
            yearly_data = self.get_yearly_average()
            if yearly_data:
                answer_parts.append("\n**Year-by-Year Breakdown:**")
                for year, value in sorted(yearly_data.items()):
                    answer_parts.append(f"- {year}: {self.format_number(value, prefix='$', suffix=' million')}")
        
        if answer_parts:
            return "\n".join(answer_parts)
        
        # Fallback: provide general statistics
        stats = self.get_summary_stats(calculation_col)
        if stats:
            answer_parts.append(f"**Statistical Summary for {calculation_col}:**")
            answer_parts.append(f"- Mean: {self.format_number(stats['mean'], prefix='$')}")
            answer_parts.append(f"- Median: {self.format_number(stats['median'], prefix='$')}")
            answer_parts.append(f"- Total: {self.format_number(stats['sum'], prefix='$')}")
            answer_parts.append(f"- Range: {self.format_number(stats['min'], prefix='$')} to {self.format_number(stats['max'], prefix='$')}")
            return "\n".join(answer_parts)
        
        return "Unable to calculate values from the provided data."
