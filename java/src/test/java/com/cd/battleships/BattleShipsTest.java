package com.cd.battleships;

import org.junit.Test;

public class BattleShipsTest {

    @Test
    public void shouldCreateNewGame() throws Exception
    {
        GameSheetFactory factory = mock(GameSheetFactory.class);

        BattleShips battleships = new BattleShips(factory);

        battleships.newGame();

        verify(factory).createGameSheet();
    }
}