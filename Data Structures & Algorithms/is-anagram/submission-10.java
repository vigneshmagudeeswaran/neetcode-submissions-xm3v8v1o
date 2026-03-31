class Solution {
    public boolean isAnagram(String s, String t) {
        
        HashMap<Character, Integer> lettersS = new HashMap<>();
        HashMap<Character, Integer> lettersT = new HashMap<>();
        if (s.length() != t.length()){
            return false;
        }
        for ( int i=0;i< s.length();i++){
            lettersS.put(s.charAt(i), lettersS.getOrDefault(s.charAt(i),0) +1);
            lettersT.put(t.charAt(i), lettersT.getOrDefault(t.charAt(i),0) +1);
        }
        return lettersS.equals(lettersT);


    }
}
