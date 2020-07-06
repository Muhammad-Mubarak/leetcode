//day 2 leet code
// reverse pailindrome integer without converting it in string
 bool isPalindrome(int x) {
        int rev=0;
        int pop =0;
        if (x == 0) return true;
        if(x %10 == 0 || x < 0  ) return false;
        while(x > rev)
        {
            pop = x%10;
            x = x/10;
            
            rev = rev * 10 +pop;
            
        }
        if(x == rev/10 || x== rev)
        {
            return true;
        }
        else
        {
            return false;
        }
        
    }
 /* 
		valid parenthesis code in java
		if (s.length() % 2 != 0) return false;
        Stack<Character> Stack = new Stack();
        for(char c : s.toCharArray()){
            if (c == '(' || c == '{' || c== '[')
                Stack.push(c);
            else if(c == ')' && !Stack.isEmpty() && Stack.peek() == '(')
                Stack.pop();
            else if(c == ']' && !Stack.isEmpty() && Stack.peek() == '[')
                Stack.pop();
            else if(c == '}' && !Stack.isEmpty() && Stack.peek() == '{')
                Stack.pop();
        }
            return Stack.isEmpty();
    }
    
 */

