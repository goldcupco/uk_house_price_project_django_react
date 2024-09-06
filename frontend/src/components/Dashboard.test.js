import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import Dashboard from './Dashboard';
import { fetchHousePriceData } from '../api/housePriceApi';

jest.mock('../api/housePriceApi');

describe('Dashboard', () => {
  it('renders the dashboard title', () => {
    render(<Dashboard />);
    expect(screen.getByText('UK House Price Dashboard')).toBeInTheDocument();
  });

  it('fetches and displays house price data', async () => {
    const mockData = [
      { date: '1995-01-01', average_price: 68, detached_price: 106, semi_detached_price: 65, terraced_price: 51, flat_price: 53 },
      { date: '2000-01-01', average_price: 102, detached_price: 160, semi_detached_price: 97, terraced_price: 78, flat_price: 87 }
    ];
    fetchHousePriceData.mockResolvedValue(mockData);

    render(<Dashboard />);

    await waitFor(() => {
      expect(fetchHousePriceData).toHaveBeenCalled();
    });

    expect(screen.getByTestId('house-price-chart')).toBeInTheDocument();
  });
});