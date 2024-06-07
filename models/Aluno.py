class Aluno:
    def __init__(self
               , Matricula  : str
               , Escola     : str
               , Nome       : str
               , Idade      : int
               , Classe     : str
               , Notas      : dict = None
               ):
        
        self.__Matricula    = Matricula
        self.__Escola       = Escola
        self.__Nome         = Nome
        self.__Idade        = Idade
        self.__Classe       = Classe
        self.__Notas        = Notas if Notas is not None else {}

    # Getters        
    @property 
    def Matricula(self): 
        return self.__Matricula								
   
    @property 
    def Escola(self): 
        return self.__Escola	
        
    @property 
    def Nome(self): 
        return self.__Nome			
    
    @property 
    def Idade(self): 
        return self.__Idade			
   
    @property 
    def Classe(self): 
        return self.__Classe			

    @property 
    def Notas(self): 
        return self.__Notas

    # Setters     
    @Matricula.setter 
    def Matricula(self, new_Matricula): 
        self.__Matricula = new_Matricula			
   
    @Escola.setter
    def Escola(self, new_Escola): 
        self.Escola = new_Escola
           
    @Nome.setter 
    def Nome(self, new_Nome): 	
        if new_Nome is None:
            self.__Nome = None
        else:
            self.__Nome = new_Nome
     
    @Idade.setter
    def Idade(self, new_Idade):   
        self.__Idade = new_Idade
 
    @Classe.setter
    def Classe(self, new_Classe):  
        self.__Classe = new_Classe

    @Notas.setter
    def Notas(self, new_Notas):
        if isinstance(new_Notas, dict):
            self.__Notas = new_Notas
        else:
            raise ValueError("Notas devem ser um dicionário")