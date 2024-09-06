import axios from 'axios';
import { fetchHousePriceData } from './housePriceApi';

jest.mock('axios');

describe('housePriceApi', () => {
  it('fetches house price data successfully', async () => {
    const mockData = [
      { date: '1995-01-01', average_price: 68, detached_price: 106, semi_detached_price: 65, terraced_price: 51, flat_price: 53 },
      { date: '2000-01-01', average_price: 102, detached_price: 160, semi_detached_price: 97, terraced_price: 78, flat_price: 87 }
    ];
    axios.get.mockResolvedValue({ data: mockData });

    const result = await fetchHousePriceData();
    expect(result).toEqual(mockData);
    expect(axios.get).toHaveBeenCalledWith('http://localhost:8000/api/price-trend-chart/');
  });

  it('handles errors when fetching house price data', async () => {
    const errorMessage = 'Network Error';
    axios.get.mockRejectedValue(new Error(errorMessage));

    await expect(fetchHousePriceData()).rejects.toThrow(errorMessage);
  });
});