from src.helpers.StrUpper import StrUpper

s = StrUpper("HELLO")

class TestStrUpper:
    def test_str1(self):
        strupper = StrUpper("bonjour")
        assert strupper.sentence == "bonjour"

    def test_str2(self):
        strupper = StrUpper("bonjour2")
        assert strupper.sentence == "bonjour2"
        
    def test_str3(self): 
        # on a fait mutter la variable sentence pour les autres tests on a brisé le principe du test qui doit être isolé
        s.sentence = "HeLLO"
        assert s.sentence == "HeLLO"
        
    def test_str4(self): 
        s = StrUpper("HELLO")
        
        assert s.sentence == "HELLO"