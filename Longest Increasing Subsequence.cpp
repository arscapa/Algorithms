#include <iostream>
#include <vector>

// Longest Increasing Subsequence
// Returns the longest length achievable as well as the subsequence itself


using namespace std;

vector<int> list = {5,7,4,-3,9,1,10,4,5,8,9,3};
vector<int> length;
vector<int> nums;


int main()
{
	for(int i = 0; i < list.size(); i++){
		// length of one item is one
		length.push_back(1);
		nums.push_back(list[i]);
		
		for(int x = 0; x < i; x++)
		{
			if (list[x] < list[i] && length[i] < 1+length[x] )
			{
				length.pop_back();
				length.push_back(1 + length[x]);
				nums.pop_back();
				nums.push_back(nums[x] + list[i]);			// most likely issue htere
			}
		}
	};	
	
	
	int maxVal = 1;
	int maxIndex = 0;
	
	for(int j = 0; j < length.size(); j++) {
		if (length[j] > maxVal)
		{
			maxVal = length[j];
			maxIndex = j;		
		}
	}
	
	
	cout << "Length of the longest increasing Subsequence is " << maxVal << endl;
	cout << "Subsequence is " << nums[maxIndex] << endl;
	
	return maxVal;
}

