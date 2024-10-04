class Solution {
    public long dividePlayers(int[] skill) {
        Arrays.sort(skill);
        int hit = skill[0]+skill[skill.length-1];
        long chem = skill[0]*skill[skill.length-1];
        for(int i = 1; i < skill.length/2; i++){
            if(skill[i] + skill[skill.length-1-i] != hit)
                return -1;
            else
                chem+= skill[i]*skill[skill.length -1 -i];
        }
        return chem;
    }
}