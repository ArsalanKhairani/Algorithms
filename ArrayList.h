/*******************************************************************************
 *                  Copyright(c) Arsalan Khairani, 2014                        *
 *                          	Linked List                                    *
 *                            	Using Array                                    *
 *                                                                             *
 * Generic array implementation of the linked list. Using built-in C++ array.  *
 *******************************************************************************/

#pragma once

template < typename ARRAYTYPE >
class ArrayList
{
protected:
	//datamembers: a pointer to array, int to store size and an int to store how many elements are used
	ARRAYTYPE *array;
	int arraySize;
	int maxElement;

public:

	//construtor with default size 10
	ArrayList(int size = 10)
	{
		arraySize = size;
		maxElement = 0;
		array = new (ARRAYTYPE [size]);
	}

	//Insert item at position specified in arguments
	void InsertItem(int position, ARRAYTYPE item)
	{
		//check if postion is within array
		if (position>arraySize){
			cout << "\nInvalid position to insert";
			return;
		}

		//right shift then insert
		for (int i = arraySize-2 ; i>position; i--)
		{
			array[i+1]= array[i];
		}
		
		array[position] = item;
		maxElement++;
	}

	//delete item from the position specified
	ARRAYTYPE DeleteItem(int position)
	{
		//again check for out side array indexing
		if (position>arraySize){
			cout << "\nInvalid position to insert";
			return NULL;
		}

		//store item to be returned
		ARRAYTYPE item = array[position];

		//left shift
		for (int i = position; i<= arraySize-1; i++)
		{
			array[i] = array[i+1];
		}

		maxElement--;
		return item;
	}

	//display whole array
	void DisplayArray()
	{
		cout << endl;
		for (int i = 0; i<arraySize; i++)
		{
			cout << array[i] << " ";
		}
	}

	//return true iff array is empty
	bool IsEmpty()
	{
		return maxElement==0;
	}

	//return true iff arrray is full
	bool IsFull()
	{
		return maxElement==arraySize;
	}

	//returns list length
	int ListLength()
	{
		return arraySize;
	}

	//delete pointer to array
	~ArrayList(void)
	{
		delete array;
	}
};

