#include <vector>
#include <algorithm>
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> temp;
        if (nums1.size() > nums2.size()){
            temp = nums1;
            for (int num : nums2){
                temp.push_back(num);
            }
        }
        else{
            temp = nums2;
            for (int num : nums1){
                temp.push_back(num);
            }
        }

        sort(temp.begin(), temp.end());

        int k = temp.size();
        if (k%2 != 0){
            return temp[(k+1)/2 - 1];
        }
        else{
            return (temp[k/2 - 1] + temp[(k/2)])/2.0;
        }

        

        
    }
};