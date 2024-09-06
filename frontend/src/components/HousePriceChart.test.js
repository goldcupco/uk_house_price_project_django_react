import React from 'react';
import { render, screen } from '@testing-library/react';
import HousePriceChart from './HousePriceChart';

describe('HousePriceChart', () => {
  const mockData = [
    { date: '1995-01-01', average_price: 68, detached_price: 106, semi_detached_price: 65, terraced_price: 51, flat_price: 53 },
    { date: '2000-01-01', average_price: 102, detached_price: 160, semi_detached_price: 97, terraced_price: 78, flat_price: 87 }
  ];

  it('renders the chart title', () => {
    render(<HousePriceChart data={mockData} />);
    expect(screen.getByText('UK House Price Trend')).toBeInTheDocument();
  });

  it('renders the chart with correct data', () => {
    render(<HousePriceChart data={mockData} />);
    expect(screen.getByTestId('chart-container')).toBeInTheDocument();
    // Add more specific assertions based on your chart library
  });

  it('displays correct labels for house types', () => {
    render(<HousePriceChart data={mockData} />);
    expect(screen.getByText('Average Price')).toBeInTheDocument();
    expect(screen.getByText('Detached Price')).toBeInTheDocument();
    expect(screen.getByText('Semi-Detached Price')).toBeInTheDocument();
    expect(screen.getByText('Terraced Price')).toBeInTheDocument();
    expect(screen.getByText('Flat Price')).toBeInTheDocument();
  });
});