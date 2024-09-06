// Dashboard.test.js
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import Dashboard from './Dashboard';

// Mock the API call
jest.mock('../api/housepriceApi', () => ({
  getHousePriceData: jest.fn(() => Promise.resolve({
    'All UK': [
      { date: '2020-01', average_price: 200000, detached_price: 300000, semi_detached_price: 250000, terraced_price: 200000, flat_price: 150000 },
      { date: '2020-02', average_price: 205000, detached_price: 310000, semi_detached_price: 255000, terraced_price: 205000, flat_price: 155000 },
    ],
    'Cambridge': [
      { date: '2020-01', average_price: 300000, detached_price: 500000, semi_detached_price: 400000, terraced_price: 350000, flat_price: 250000 },
      { date: '2020-02', average_price: 310000, detached_price: 520000, semi_detached_price: 410000, terraced_price: 360000, flat_price: 260000 },
    ],
  }))
}));

describe('Dashboard', () => {
  test('renders dashboard with dropdown and charts', async () => {
    render(<Dashboard />);
    
    expect(screen.getByLabelText('Select Area')).toBeInTheDocument();
    
    await waitFor(() => {
      expect(screen.getByTestId('average-price-chart')).toBeInTheDocument();
      expect(screen.getByTestId('relative-change-chart')).toBeInTheDocument();
      expect(screen.getByTestId('property-types-chart')).toBeInTheDocument();
      expect(screen.getByTestId('property-types-relative-change-chart')).toBeInTheDocument();
    });
  });

  test('dropdown contains all specified areas', () => {
    render(<Dashboard />);
    const areas = [
      'All UK', 'Cambridge', 'Stevenage', 'Inner London', 'Sheffield', 'Bradford',
      'Leeds', 'York', 'Manchester', 'Salford', 'Nottingham', 'Bristol', 'Edinburgh',
      'Glasgow', 'Newcastle', 'Preston', 'Lancaster', 'Cardiff', 'Chester', 'Birmingham',
      'Northampton', 'Rugby', 'Walsall'
    ];
    
    areas.forEach(area => {
      expect(screen.getByText(area)).toBeInTheDocument();
    });
  });

  test('selecting an area updates all charts', async () => {
    render(<Dashboard />);
    const dropdown = screen.getByLabelText('Select Area');
    
    fireEvent.change(dropdown, { target: { value: 'Cambridge' } });
    
    await waitFor(() => {
      expect(screen.getByTestId('average-price-chart')).toHaveTextContent('HPI - Average Price of Properties in Cambridge');
      expect(screen.getByTestId('relative-change-chart')).toHaveTextContent('HPI - Relative Cumulative Change of Average Price of Properties in Cambridge');
      expect(screen.getByTestId('property-types-chart')).toHaveTextContent('HPI - Average Price of Property Types in Cambridge');
      expect(screen.getByTestId('property-types-relative-change-chart')).toHaveTextContent('HPI - Relative Cumulative Change of Average Price of Property Types in Cambridge');
    });
  });

  test('charts display correct axes labels', async () => {
    render(<Dashboard />);
    
    await waitFor(() => {
      expect(screen.getByTestId('average-price-chart')).toHaveTextContent('Average Price (£)');
      expect(screen.getByTestId('average-price-chart')).toHaveTextContent('Transaction Date');
      
      expect(screen.getByTestId('relative-change-chart')).toHaveTextContent('growth_since_95');
      expect(screen.getByTestId('relative-change-chart')).toHaveTextContent('Transaction Date');
      
      expect(screen.getByTestId('property-types-chart')).toHaveTextContent('Average Price (£)');
      expect(screen.getByTestId('property-types-chart')).toHaveTextContent('Transaction Date');
      
      expect(screen.getByTestId('property-types-relative-change-chart')).toHaveTextContent('growth_since_95');
      expect(screen.getByTestId('property-types-relative-change-chart')).toHaveTextContent('Transaction Date');
    });
  });

  test('charts display as line graphs', async () => {
    render(<Dashboard />);
    
    await waitFor(() => {
      expect(screen.getByTestId('average-price-chart')).toHaveAttribute('data-testid', 'line-chart');
      expect(screen.getByTestId('relative-change-chart')).toHaveAttribute('data-testid', 'line-chart');
      expect(screen.getByTestId('property-types-chart')).toHaveAttribute('data-testid', 'line-chart');
      expect(screen.getByTestId('property-types-relative-change-chart')).toHaveAttribute('data-testid', 'line-chart');
    });
  });
});