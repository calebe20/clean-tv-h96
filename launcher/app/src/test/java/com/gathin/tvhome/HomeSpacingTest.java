package com.gathin.tvhome;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class HomeSpacingTest {
    @Test public void disabledCapKeepsOriginalPlacement() {
        assertEquals(220, HomeSpacing.topPadding(220, 0, 140, 1.33f));
    }

    @Test public void titleClearanceWinsOnShortScreens() {
        assertEquals(140, HomeSpacing.topPadding(220, 50, 140, 1.33f));
    }

    @Test public void visibleNamesKeepTheirSpace() {
        assertEquals(12, HomeSpacing.bottomOffset(-12, true));
        assertEquals(-12, HomeSpacing.bottomOffset(-12, false));
    }
}
