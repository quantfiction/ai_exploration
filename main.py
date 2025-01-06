from portfolio_optimizer import PortfolioOptimizer

def main():
    # Initialize portfolio optimizer with 1% risk units
    optimizer = PortfolioOptimizer(risk_unit_pct=0.01)
    
    # Add assets with expected returns, risks, and position types
    optimizer.add_asset("Stock A", expected_return=0.12, risk=0.20, position_type='long')
    optimizer.add_asset("Stock B", expected_return=0.08, risk=0.15, position_type='long')
    optimizer.add_asset("Bond C", expected_return=0.05, risk=0.08, position_type='long')
    optimizer.add_asset("Crypto D", expected_return=0.20, risk=0.40, position_type='short')
    
    # Calculate position sizes for $100,000 portfolio
    total_capital = 100000
    position_sizes = optimizer.calculate_position_sizes(total_capital)
    
    # Display results
    print("\nPortfolio Summary:")
    print("=================")
    print(f"Total Capital: ${total_capital:,.2f}")
    print(f"Risk Unit Size: ${total_capital * 0.01:,.2f} (1% of portfolio)")
    
    print("\nOptimal Positions:")
    print("-----------------")
    for asset, size in position_sizes.items():
        position_type = 'Long' if size >= 0 else 'Short'
        allocation = (abs(size) / total_capital) * 100
        risk_units = abs(size) * optimizer.risk_unit_pct / (total_capital * optimizer.risk_unit_pct)
        
        print(f"{asset} ({position_type}):")
        print(f"  Size: ${abs(size):,.2f}")
        print(f"  Allocation: {allocation:.1f}%")
        print(f"  Risk Units: {risk_units:.2f}")
        
    print("\nPortfolio Metrics:")
    print("-----------------")
    total_risk_units = sum(
        abs(size) * optimizer.risk_unit_pct / (total_capital * optimizer.risk_unit_pct)
        for size in position_sizes.values()
    )
    print(f"Total Risk Units: {total_risk_units:.2f}")

if __name__ == "__main__":
    main()
