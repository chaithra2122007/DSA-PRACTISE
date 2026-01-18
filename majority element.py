#leetcode submission link : https://leetcode.com/problems/majority-element/post-solution/?submissionId=1840594767
class Solution {
public:
    bool containsDuplicate(vector<int>& nums)
    {
        int i,j;
        sort(nums.begin(),nums.end());
        int n=nums.size();
        for(i=0;i<n-1;i++)
        {
            if(nums[i]==nums[i+1])
                return true;   
        } 
        return false;  
    }
    
};
