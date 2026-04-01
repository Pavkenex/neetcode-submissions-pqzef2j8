class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<char>> rowAppeared(9);
        vector<set<char>> columnAppeared(9);
        vector<set<char>> squareAppeared(9);
        
        for(int i = 0; i < 9; i++){
           for(int j = 0; j < 9; j++){
               
               char trenutniBroj = board[i][j];

               // 1. OBAVEZNO: Preskoči prazna polja!
               if (trenutniBroj == '.') {
                   continue;
               }

               // Računamo indeks kvadrata (0-8)
               int squareIndex = (i / 3) * 3 + (j / 3);

               // 2. Provera: Da li smo već videli ovaj broj u redu, koloni ili kvadratu?
               // Pazi: Za kolonu koristimo indeks 'j', jer smo u j-toj koloni.
               if(rowAppeared[i].count(trenutniBroj) > 0 || 
                  columnAppeared[j].count(trenutniBroj) > 0 ||
                  squareAppeared[squareIndex].count(trenutniBroj) > 0){
                    return false;
               }
                
               // 3. Ubacivanje
               rowAppeared[i].insert(trenutniBroj);  
               columnAppeared[j].insert(trenutniBroj); // Ubacujemo u j-ti set za kolone
               squareAppeared[squareIndex].insert(trenutniBroj);
            }
        }
        return true;
    }
};