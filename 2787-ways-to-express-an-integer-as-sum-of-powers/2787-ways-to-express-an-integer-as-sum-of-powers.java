class Solution {

    public static int mod = 1000000007;

    public static int solve(int[][] dp , ArrayList<Integer> arr , int n , int i)
    {
        if(n == 0)
            return 1;
        if(i == arr.size())
            return 0;
        if(dp[i][n] != -1)
            return dp[i][n];
        int take = 0;
        if(arr.get(i) <= n)
            take = solve(dp , arr , n-arr.get(i) , i+1) % mod;
        int not_take = solve(dp , arr , n , i+1) % mod;
        dp[i][n] = (take+not_take) % mod;
        return dp[i][n];
    }

    public int numberOfWays(int n, int x) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for(int i = 1; i <= n ; i++)
        {
            int temp = (int)Math.pow(i,x);
            if(temp <= n)
                ans.add(temp);
            else
                break;
        }
        int dp[][] = new int[ans.size()+1][n+1];
        for(int[] z : dp)
            Arrays.fill(z ,-1);
        return solve(dp , ans , n, 0);
    }
}