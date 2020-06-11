import pytest
from utils.spaCy_analysis import spaCy_analysis

class TestSpaCyAnalisys:

    def test_spaCy_analysis(self):
        form_input = 'Hello World'

        def dummy_getter(id):
            return {
                'article_title': 'Josiane',
                'article_intro': 'Josiane habite à Nantes depuis 1908',
                'article_content': 'Fille de Jules et Gabrielle Bertin, Emilienne Bertin(dite Lelette) fut agent de renseignement pour la Résistance. Avec sa soeur Marthe, elle hébergea des militants communistes clandestins tels Gaston Plissonnier, Josette Billoux* et Fernande Valignat*. Son père, également militant communiste, fut arrêté, torturé et assassiné par l’occupant nazi. À partir de la Libération, Emilienne Bertin anima l’Association nationale des anciens combattants de la résistance (ANACR) dans la région de Gannat, tout en militant à la cellule André Cavard de la section du PCF de Gannat. Sa soeur épousa Roger Sandrier ; résistant communiste, dont le fils, Jean-Claude Sandrier, devint maire et député communiste de Bourges. Malade, Emilienne Bertin décéda le 27 octobre 1993 et fut inhumée au cimetière de Lalizolle (Allier).',
            }
        spaCy_response = spaCy_analysis(string_to_analyse=form_input, article_getter=dummy_getter)
        expected = {'Gannat', 'Lalizolle', 'de Bourges', 'Allier', 'Nantes'}
        assert spaCy_response == expected
        assert isinstance(spaCy_response, set)