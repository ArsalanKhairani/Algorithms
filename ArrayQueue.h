/*******************************************************************************
 *                  Copyright(c) Arsalan Khairani, 2014                        *
 *                          	   Queue                                 	   *
 *                            	Using Array                                    *
 *                                                                             *
 * Generic array implementation of Queue. 							 		   *
 * Based on Array List implementation. 										   *
 *******************************************************************************/

#pragma once
#include "arraylist.h"

template < typename ARRAYTYPE >
class ArrayQueue :
	public ArrayList<ARRAYTYPE>
{
	int total;
	int filled;

public:

	ArrayQueue(void)
	{
		total = 10;
		filled = 0;
		array = new (ARRAYTYPE [total]);
	}

	//add an item to the top of the queue
	void Enqueue(ARRAYTYPE item)
	{
		InsertItem(filled, item);
		filled++;
	}

	//remove an item from the bottom of the queue
	void Dequeue()
	{
		DeleteItem(0);
		filled--;
	}

	//display whole array Queue
	void DisplayArrayQueue()
	{
		cout << endl;
		for (int i = filled -1; i>=0; i--)
		{
			cout << array[i] << " ";
		}
	}

	~ArrayQueue(void)
	{
	}
};

