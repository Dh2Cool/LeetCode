class Solution {
    int convert(char ch){
        switch(ch){
            case 'I':
                return 1;
            case 'V':
                return 5;
            case 'X':
                return 10;
            case 'L':
                return 50;
            case 'C':
                return 100;
            case 'D':
                return 500;
            case 'M':
                return 1000;
            default:
                return 0;
        }
    }
    public int romanToInt(String s) {
        int res = 0;
        for(int i = 0; i<s.length(); i++){
            char ch = s.charAt(i);
            if(i != s.length()-1){
                char ch1 = s.charAt(i+1);
                if(convert(ch1) > convert(ch)){
                    res += convert(ch1)-convert(ch);
                    i++;
                }
                else{
                    res+= convert(ch);
                }
            }
            else{
                res+= convert(ch);
            }
        }
        
        return res;
    }
}