/*******************************************************************************
 *                  Copyright(c) Arsalan Khairani, 2014                        *
 *                          	   Stack                                       *
 *                            	Using Array                                    *
 *                                                                             *
 * Generic array implementation of Stack. 				       *
 * Based on Array List implementation. 					       *
 *******************************************************************************/

#pragma once
#include "arraylist.h"

template < typename ARRAYTYPE >
class ArrayStack :
	public ArrayList<ARRAYTYPE>
{
	ARRAYTYPE* stackPointer;
	int total;
	int filled;

public:
	ArrayStack ()
	{
		total = 10;
		filled = 0;
		array = new (ARRAYTYPE [total]);
		stackPointer = array;
	}

	//add an item to the top of the stack
	void Push(ARRAYTYPE item)
	{
		InsertItem(filled, item);
		stackPointer = &stackPointer[++filled];
	}
	
	//remove an item from the top of the stack
	ARRAYTYPE Pop()
	{
		stackPointer = &stackPointer[filled];
		return DeleteItem(--filled);
	}

	//display whole array Stack
	void DisplayArrayStack()
	{
		cout << endl;
		for (int i = filled-1; i>=0; i--)
		{
			cout << array[i] << " ";
		}
	}

	~ArrayStack(void)
	{
	}
};

