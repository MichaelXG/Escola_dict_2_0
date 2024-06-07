class Escola:
    def __init__(self
               , CodEscola      : int
               , Nome           : str
                ):
        self.__CodEscola    = CodEscola
        self.__Nome         = Nome

    # Getters
    @property 
    def CodEscola(self): 
        return self.__CodEscola

    @property 
    def Nome(self): 
        return self.__Nome			
    
    # Setters     
    @CodEscola.setter 
    def CodEscola(self, new_CodEscola): 
        self.__CodEscola = new_CodEscola
    
    @Nome.setter 
    def Nome(self, new_Nome): 	
        self.__Nome = new_Nome