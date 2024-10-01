class Solution {
    public boolean isPalindrome(String s) {
        String str = "";
        for(int i = 0; i<s.length();i++){
            char ch = s.charAt(i);
            if(Character.isLetterOrDigit(ch)){
                str = str + Character.toLowerCase(ch);
            }
        }
        System.out.println(str);
        for(int i = 0, j=str.length()-1; i<str.length()/2; i++){
            char chi = str.charAt(i);
            char chj = str.charAt(j);
            if(chi != chj)
                return false;
            j--;
        }
        return true;
    }
}