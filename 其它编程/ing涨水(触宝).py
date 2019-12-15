# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 18:38
# @Author  : Liling
'''
涨水
'''
public class Main{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int height=in.nextInt(),width=in.nextInt();
        int waterLevel=in.nextInt();
        int [][]map=new int[height][width];
        for(int i=0;i<height;i++){
            for(int j=0;j<width;j++){
                map[i][j]=in.nextInt();
            }
        }
        boolean [][]isVisited=new boolean[height][width];
        for(int i=0;i<height;i++){
            if(!isVisited[i][0])
                dfs(map,isVisited,i,0,waterLevel);
            if(!isVisited[i][width-1])
                dfs(map,isVisited,i,width-1,waterLevel);
        }
        for(int j=1;j<width-1;j++){
            if(!isVisited[0][j])
                dfs(map,isVisited,0,j,waterLevel);
            if(!isVisited[height-1][j])
                dfs(map,isVisited,height-1,j,waterLevel);
        }
        int countExist=0;
        for(int i=0;i<height;i++)
            for(int j=0;j<width;j++)
                if(map[i][j]!=0) countExist++;
        System.out.println(countExist);
        in.close();
    }
    private static void dfs(int [][]map,boolean [][]isVisited,int i,int j,int waterLevel){
        if(i<0||i>=map.length||j<0||j>=map[0].length||isVisited[i][j]) return ;
        isVisited[i][j]=true;
        if(waterLevel<map[i][j]) return ;
        else map[i][j]=0;
        dfs(map,isVisited,i+1,j,waterLevel);
        dfs(map,isVisited,i-1,j,waterLevel);
        dfs(map,isVisited,i,j+1,waterLevel);
        dfs(map,isVisited,i,j-1,waterLevel);
    }
}