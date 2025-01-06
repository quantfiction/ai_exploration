import numpy as np
import pandas as pd
from typing import List, Dict

class PortfolioOptimizer:
    def __init__(self, risk_unit_pct: float = 0.01):
        """
        Args:
            risk_unit_pct: Percentage of portfolio value representing one unit of risk (default: 1%)
        """
        self.assets = []
        self.convictions = []
        self.risk_unit_pct = risk_unit_pct
        self.cov_matrix = None
        
    def add_asset(self, asset_name: str, expected_return: float, risk: float, position_type: str = 'long'):
        """
        Add an asset with its expected return and risk
        Args:
            asset_name: Name of the asset
            expected_return: Expected return (as decimal)
            risk: Risk (standard deviation as decimal)
            position_type: 'long' or 'short'
        """
        if position_type not in ['long', 'short']:
            raise ValueError("position_type must be 'long' or 'short'")
            
        self.assets.append(asset_name)
        self.convictions.append((expected_return, risk, position_type))
        
    def calculate_position_sizes(self, total_capital: float, risk_tolerance: float = 1.0) -> Dict[str, float]:
        """
        Calculate optimal position sizes using risk-adjusted returns
        Args:
            total_capital: Total capital to allocate
            risk_tolerance: Risk tolerance factor (0.0 to 1.0)
        Returns:
            Dictionary of asset names to position sizes
        """
        if not self.assets:
            raise ValueError("No assets added to portfolio")
            
        # Convert convictions to numpy arrays
        returns = np.array([c[0] for c in self.convictions])
        risks = np.array([c[1] for c in self.convictions])
        position_types = np.array([c[2] for c in self.convictions])
        
        # Calculate risk-adjusted returns
        risk_adjusted_returns = returns / (risks ** risk_tolerance)
        
        # Normalize to get weights
        weights = risk_adjusted_returns / risk_adjusted_returns.sum()
        
        # Calculate position sizes in risk units
        risk_units = {asset: weight * (total_capital * self.risk_unit_pct)
                     for asset, weight in zip(self.assets, weights)}
        
        # Calculate dollar positions based on risk units
        position_sizes = {}
        for i, asset in enumerate(self.assets):
            position_size = risk_units[asset] / risks[i]
            if position_types[i] == 'short':
                position_size *= -1
            position_sizes[asset] = position_size
            
        return position_sizes
