class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        for(int i =0; i < participant.length; i++){
            for(int j = 0; j< completion.length; j++){
                if(completion[j].equals(participant[i])){
                    participant[i] = "s";
                    completion[j] ="k";
                    break;
                }
            }
        }
        for(int i =0; i < participant.length; i++){
           if(participant[i].equals("s")== false ){
             System.out.println(participant[i]);
               answer = participant[i];
           }
        }
        return answer;
    }
}