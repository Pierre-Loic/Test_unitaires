import unittest
from unittest.mock import patch
from math import pi
from hypothesis import given
import hypothesis.strategies as st
import Exercices as ex

class Exercice_1_Test_case(unittest.TestCase):

    @given(st.integers(), st.integers())
    def test_positif(self, x, y):
        # print(f"x = {x} et y = {y}")
        self.assertEqual(ex.exercice_1(x, y), x*y)

    @given(st.integers(), st.integers())
    def test_negatif(self, x, y):
        self.assertEqual(ex.exercice_1(-x, y), -x*y)

    def test_nul(self):
        self.assertEqual(ex.exercice_1(0, 200), 0)
        self.assertEqual(ex.exercice_1(0, 0), 0)
        self.assertEqual(ex.exercice_1(0, -500), 0)

    def test_str(self):
        self.assertRaises(TypeError, ex.exercice_1, "abc", "def")
        self.assertRaises(TypeError, ex.exercice_1, "abc", 0)
        self.assertRaises(TypeError, ex.exercice_1, 10, "")

class Exercice_2_Test_case(unittest.TestCase):

    def test_inf(self):
        self.assertEqual(ex.exercice_2(-2, 1, 2), -255)
        self.assertEqual(ex.exercice_2(-1000, 10, 15), -255)
        self.assertEqual(ex.exercice_2(-10, -5, 2), -255)
        self.assertEqual(ex.exercice_2(-15, -10, -2), -255)

    def test_in(self):
        self.assertEqual(ex.exercice_2(1, 1, 2), 1)
        self.assertEqual(ex.exercice_2(2, 1, 2), 2)
        self.assertEqual(ex.exercice_2(5, 1, 10), 5)
        self.assertEqual(ex.exercice_2(-5, -6, 2), -5)

    def test_sup(self):
        self.assertEqual(ex.exercice_2(3, 1, 2), 255)
        self.assertEqual(ex.exercice_2(5, -1, 2), 255)
        self.assertEqual(ex.exercice_2(-2, -10, -5), 255)
        self.assertEqual(ex.exercice_2(5, 2, 2), 255)

    def test_str(self):
        self.assertRaises(TypeError, ex.exercice_2, "abc", "def", "ghi")
        self.assertRaises(TypeError, ex.exercice_2, "abc", 0, 2)
        self.assertRaises(TypeError, ex.exercice_2, 10, "", "abc")

class Exercice_3_Test_case(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Début")

    @classmethod
    def tearDownClass(cls):
        print("Fin")
    
    def setUp(self):
        self.exo = ex.Exercice_3()

    def tearDown(self):
        print("Fin du test")
    
    def test_r_num(self):
        self.assertEqual(self.exo.r_num(10), None)
        self.assertEqual(self.exo.r, 10)
        self.assertRaises(TypeError, self.exo.r_num, "abc")
        self.assertRaises(ValueError, self.exo.r_num, -5)

    def test_aire(self):
        self.assertAlmostEqual(self.exo.aire(10), pi*10**2)
        self.assertEqual(self.exo.aire(0), 0)
        self.assertRaises(TypeError, self.exo.aire, "abc")
        self.assertRaises(ValueError, self.exo.aire, -8)

    def test_perimetre(self):
        self.assertAlmostEqual(self.exo.perimetre(5), 2*pi*5)
        self.assertEqual(self.exo.perimetre(0), 0)
        self.assertRaises(TypeError, self.exo.perimetre, "abc")
        self.assertRaises(ValueError, self.exo.perimetre, -8)

    def test_dans_cercle(self):
        self.assertTrue(self.exo.dans_cercle(2, 0, 1))
        self.assertTrue(self.exo.dans_cercle(2, 1, 0))
        self.assertTrue(self.exo.dans_cercle(2, 1, 1))
        self.assertTrue(self.exo.dans_cercle(2, -1, -1))
        self.assertFalse(self.exo.dans_cercle(2, 2, 2))
        self.assertFalse(self.exo.dans_cercle(2, -3, 2))
        self.assertRaises(TypeError, self.exo.dans_cercle, "abc", 3, 4)
        self.assertRaises(TypeError, self.exo.dans_cercle, 8, "abc", 4)
        self.assertRaises(TypeError, self.exo.dans_cercle, 8, 56, "abc")
        self.assertRaises(ValueError, self.exo.dans_cercle, -8, 2, 3)
    
class Exercice_4_Test_case(unittest.TestCase):

    def test_init(self):
        with patch("Exercices.requests.get") as mocked_get:
            exo = ex.Exercice_4("Paris")
            mocked_get.assert_called_with("https://fr.wikipedia.org/w/api.php",
                                          params={
                                                "search": "Paris",
                                                "format": "json",
                                                "action": "opensearch", 
                                              })
    def test_loc(self):
        fake_answer = ["Paris",["Paris","Paris Saint-Germain Football Club","Paris Football Club","Paris Hilton","Paris-Gare-de-Lyon","Paris Saint-Germain Handball","Paris Saint-Germain Football Club (f\u00e9minines)","Paris Match","Paris-Saclay","Paris sous l'occupation allemande"],["Paris est la capitale de la France","Paris Saint-Germain ou PSG, est un club de football fran\u00e7ais faisant partie du club omnisports du m\u00eame nom, bas\u00e9 \u00e0 Saint-Germain-en-Laye et \u00e0 Paris.","Le Paris Football Club, abr\u00e9g\u00e9 en Paris FC ou PFC, est un club de football fran\u00e7ais bas\u00e9 \u00e0 Paris et \u00e0 Orly.","Paris Hilton, n\u00e9e le 17 f\u00e9vrier 1981 \u00e0 New York, est une femme d'affaires, personnalit\u00e9 m\u00e9diatique, mannequin, chanteuse, actrice et disc jockey am\u00e9ricaine, consid\u00e9r\u00e9e comme une jet setteuse ou comme une \u00ab socialite \u00bb.","Paris-Gare-de-Lyon est l'une des sept gares terminus du r\u00e9seau de la SNCF \u00e0 Paris. C'est aussi une gare du r\u00e9seau RER d'\u00cele-de-France.","La section handball du Paris Saint-Germain (couramment abr\u00e9g\u00e9 en Paris SG ou PSG) est un club de handball fran\u00e7ais bas\u00e9 \u00e0 Paris.","La section football f\u00e9minin du Paris Saint-Germain, couramment abr\u00e9g\u00e9 en Paris SG ou PSG, est un club de football fran\u00e7ais bas\u00e9 \u00e0 Paris et cr\u00e9\u00e9 en 1971. Le principal titre du club \u00e9tait une Coupe de France remport\u00e9e en 2010 face \u00e0 Montpellier, avant que le club ne remporte en 2018 sa seconde Coupe de France, et mette ainsi fin au r\u00e8gne de l'OL dans cette comp\u00e9tition (1-0).","Paris Match est un magazine hebdomadaire fran\u00e7ais d\u2019actualit\u00e9s et d\u2019images, n\u00e9 en 1949 et c\u00e9l\u00e8bre par sa devise : \u00ab Le poids des mots, le choc des photos \u00bb.","Paris-Saclay est un p\u00f4le scientifique et technologique (cluster) en cours d'am\u00e9nagement \u00e0 vingt kilom\u00e8tres au sud de Paris, sur une zone couvrant 27 communes des d\u00e9partements de l'Essonne et des Yvelines.","Paris subit l'occupation allemande entre le 14 juin 1940 (arriv\u00e9e des troupes allemandes) et le 24 ao\u00fbt 1944 (entr\u00e9e de la 2e DB)."],["https://fr.wikipedia.org/wiki/Paris","https://fr.wikipedia.org/wiki/Paris_Saint-Germain_Football_Club","https://fr.wikipedia.org/wiki/Paris_Football_Club","https://fr.wikipedia.org/wiki/Paris_Hilton","https://fr.wikipedia.org/wiki/Paris-Gare-de-Lyon","https://fr.wikipedia.org/wiki/Paris_Saint-Germain_Handball","https://fr.wikipedia.org/wiki/Paris_Saint-Germain_Football_Club_(f%C3%A9minines)","https://fr.wikipedia.org/wiki/Paris_Match","https://fr.wikipedia.org/wiki/Paris-Saclay","https://fr.wikipedia.org/wiki/Paris_sous_l%27occupation_allemande"]]
        with patch("Exercices.requests.get") as mocked_get:
            mocked_get.return_value.json.return_value = fake_answer
            exo = ex.Exercice_4("Paris")
            self.assertEqual(exo.loc(), "Voici ce que je connais de Paris : Paris est la capitale de la France")
        
if __name__=="__main__":
    unittest.main()
