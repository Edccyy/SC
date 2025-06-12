from .optimisation import optimisation
from .ilfautunnom import besoins

"""
Ce fichier contient les tests de la fonction `optimisation`.
"""

nouveau_besoins = besoins(
    proteines=50,
    lipides=70,
    glucides=300,
    calories=000,
    fer=10,
    calcium=800,
    fibres=30
)

def test_optimisation():
    """
    Test de la fonction `optimisation`.
    """
    result = optimisation(nouveau_besoins)
    
    # Vérification que le résultat est un DataFrame
    assert isinstance(result, pd.DataFrame), "Le résultat doit être un DataFrame"
    
    # Vérification que le DataFrame contient les colonnes attendues
    expected_columns = ['Nutriment', 'Besoins', 'Apport obtenu', '% des besoins']
    assert all(col in result.columns for col in expected_columns), "Le DataFrame doit contenir les colonnes attendues"
    
    # Vérification que les apports obtenus sont conformes aux besoins
    for index, row in result.iterrows():
        assert row['Apport obtenu'] >= 0, "Les apports obtenus doivent être positifs"
        assert row['% des besoins'] >= 0, "Le pourcentage des besoins doit être positif"