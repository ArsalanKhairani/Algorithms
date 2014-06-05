/*******************************************************************************
 *                  Copyright(c) Arsalan Khairani, 2014                        *
 *                            Towers Of Hanoi                                  *
 *                                                                             *
 * Recursive algorithm for solving towers of hanoi. Using Linked-list as towers*
 *******************************************************************************/

#include <iostream>
#include "ListStack.h"
using namespace std;

ListStack<string> TowerA;
ListStack<string> TowerB;
ListStack<string> TowerC;
int steps = 0;

void DisplayTowers()
{
	cout << "\n\n\n\t\t\t\tStep " << steps++;
	cout << "\nTower A:\n";
	TowerA.DisplayListStack();
	cout << "\nTower B:\n";
	TowerB.DisplayListStack();
	cout << "\nTower C:\n";
	TowerC.DisplayListStack();
}

void Solve(int height, ListStack<string>* Beg, ListStack<string>* Aux, ListStack<string>* End)
{
	if (height == 1) 
	{
		End->Push(Beg->Pop());
		DisplayTowers();
		return;
	}
	Solve(height-1,Beg, End, Aux);
	End->Push(Beg->Pop());
	DisplayTowers();
	Solve(height-1,Aux, Beg, End);
	
	return;
}

void Input()
{
	int height;
	cout << "\nEnter height of tower: ";
	cin >> height;
	for (int i=height; i>0; i--)
	{
		string ent;
		for (int j=1; j<=i; j++)
			ent += "z";
		TowerA.Push(ent);
	}
	DisplayTowers();
	Solve(height, &TowerA, &TowerB, &TowerC);
}
