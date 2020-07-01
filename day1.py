#duplicate zeros in an array in  python
 # def duplicateZeros(self, arr: List[int]) -> None:
 #        i = 0;
        
 #        while i < len(arr):
 #            if arr[i] !=0:
 #                i+=1
 #            else:
                
 #                arr.insert(i+1, 0)
 #                i+=2
 #                arr.pop()


 ## following is the code in ruby for duplicate zeros
#  def duplicate_zeros(arr)
#     i =0
#     while i< arr.length() do
#         if arr[i] !=0
#             i+=1
#         else
#             arr.insert(i+1,0)
#             i+=2
#             arr.pop()
#         end
#     end
    
# end


#merging of 2 sorted arrays in c++
 # void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
      
 #        int first = m-1;
 #        int second = n-1;
 #        for (int i = m+n-1; i>=0; i--)
 #        {
 #            if(second < 0)
 #            {
 #                break;
 #            }
 #            if(nums1[first] > nums2[second])
 #            {
 #                nums1[i] = nums1[first];
 #                first--;
 #            }
 #            else{
 #                nums1[i] = nums2[second];
 #                second--;
 #            }
 #        }
 #    }
