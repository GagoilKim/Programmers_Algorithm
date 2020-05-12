class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int one = 0;
        int two = 0;
        int three = 0;
        int [] onevalue = {1, 2, 3, 4, 5};
        int [] twovalue = {2,1,2,3,2,4,2,5};
        int [] threevalue = {3,3,1,1,2,2,4,4,5,5};
        one = match(onevalue, answers);
        two = match(twovalue, answers);
        three = match(threevalue, answers);
        if(one > two && one>  three){
            answer = new int[1];
            answer[0] = 1;
        }else if(two > one && two> three){
                        answer = new int[1];

            answer[0] = 2;
        }else if(three > one && three > two){
                        answer = new int[1];

            answer[0] = 3;
        }else{
            if(one==two && one> three){
                                        answer = new int[2];
                answer[0] = 1;
                answer[1] = 2;
            }else if(one == three&& one > two){
                                       answer = new int[2];
                answer[0] = 1;
                answer[1] = 3;
            }else if(two == three && two > one){
                                       answer = new int[2];
                answer[0] = 2;
                answer[1] = 3;
            }else{
                              answer = new int[3];

            answer[0] = 1;
            answer[1] = 2;
            answer[2] = 3;
            }
          
        }
        return answer;
    }
    public int match(int[] value, int[]answers){
        int count = 0;
        int j = 0;
        for(int i = 0; i < answers.length; i ++ ){
            if(answers[i] == value[j]){
                count++;
            }    
            j++;
            if(j == value.length){
                j = 0;
            }
        }
        return count;
    }
}