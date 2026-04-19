class NumMatrix {
private:
    vector<vector<int>> sumMat;
public:
    NumMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        sumMat = vector<vector<int>>(n+1, vector<int>(m+1,0));
        for(int i=0; i<n; i++){
            int prefix = 0;
            for(int j=0; j<m; j++){
                prefix += matrix[i][j];
                sumMat[i+1][j+1] = sumMat[i][j+1] + prefix;
            }
        }
        // for(int i=0; i<=n; i++){
        //     for(int j=0; j<=m; j++){
        //         cout<<sumMat[i][j]<<" ";
        //     }
        //     cout<<endl;
        // }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int last = sumMat[row2+1][col2+1];
        int top = sumMat[row1][col1];
        int x1 = sumMat[row1][col2+1];
        int x2 = sumMat[row2+1][col1];
        return top+last-x1-x2;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */