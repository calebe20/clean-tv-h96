package com.gathin.tvhome;

/** Spacing limits shared by the grid placement and its dock decoration. */
final class HomeSpacing {
    private HomeSpacing() { }

    static int topPadding(int natural, int capDp, int clearance, float density) {
        if (capDp <= 0) return natural;
        return Math.max(clearance, Math.min(natural, Math.round(capDp * density)));
    }

    static int bottomOffset(int requestedDp, boolean namesVisible) {
        return namesVisible ? Math.max(12, requestedDp) : requestedDp;
    }
}
