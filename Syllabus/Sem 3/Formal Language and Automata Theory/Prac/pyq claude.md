
I'll help you with the answers:

Group A (1 mark each):

1. (i) 2^n - When converting NFA to DFA, maximum possible states is 2^n
2. (ii) Finite State Machine - Transition table represents FSM
3. (iii) Unique path to all other state for every input symbol - This is the definition of DFA
4. (iv) Moore Machine - A shift register is a type of Moore machine
5. (v) 0 - Finite automata (FA) doesn't require any stacks
6. (vi) Type 3 Grammar - Regular grammar is Type 3
7. (vii) 16 - For 2 states and binary input (0,1), total possible DFAs = 2^(2*2) = 16
8. (viii) The set of all strings containing at least two 1's
9. (ix) L is not a regular language - a^nb^n is not regular
10. (x) Must contain any combination of a,b or null string - This is what a*(a+b)* represents

For Group B and C, here are key solutions:

5. Pumping Lemma proof for L={a^nb^n | n>=1}:
   - Assume L is regular with pumping length p
   - Take string s = a^pb^p
   - Split into xyz where |xy|≤p
   - Then y must contain only a's
   - Pumping y will create more a's than b's
   - Therefore L is not regular

6. For DFA with 'a' immediately preceded and followed by 'b':
   - Need states to track if we've seen 'b' before 'a'
   - Need to ensure 'b' follows 'a'
   - Draw states with appropriate transitions

Would you like me to explain any of these in more detail or help with other questions?
