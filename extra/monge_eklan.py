import jellyfish as j

class MongeEklan():
    '''
    Accepts the inner similarity function
    '''
    def __init__(self):
        pass
    
    def score(self,q1,q2,m):
        '''
        Input: s - multi-word string
               t - multi-word string
               m - power
        Output : score
        Note: In single word string, score = jaro-winkler score
        '''
        cummax = 0
        
        for ws in q1.split(" "):
            maxscore=0
            for wt in q2.split(" "):
                maxscore = max(maxscore,(j.jaro_winkler(ws,wt))**m)
            cummax += maxscore
        
        return (cummax/len(q1.split(" ")))**(1/m)
        
def main():
    m = MongeEklan()
    print(m.score("peter christen","christian pedro", m=1))
    print(m.score("paul johnson","johson paule",m=1))
    
if __name__ == '__main__':
    main()
