# Power supply dimensions and mechanical compatibility

Dimensions are **length × width × height in millimeters**. The housing dimensions describe the finished printed enclosure. The supply dimensions describe the electronic assembly that goes inside it.

| Case | Supply dimensions and origin | Design allowance | Printed exterior |
|---|---|---|---|
| [Delta iMac 27″ Late 2015 Power Supply](../cases/imac-27-5k-2015/) | Delta ADP-300AF T PCB, estimated from photographs at 163 ± 1 × 132 ± 2, maximum component height 30 ± 5 | 164 × 134 in plan, 35 above the board mounting plane | 190 × 166 × 50 including feet |
| [AURA S-60-12](../cases/aura-s60/) | 86 × 58.02 × 33.02, bounding box of the supplied 44-solid STEP assembly | Designed around that metal housing and its terminal end | 148 × 88 × 42.8 |
| [AURA Compact 160](../cases/aura-compact-160/) | Metal housing estimated at 110 × 98–100 × 35–36 | Upper envelope 112 × 102 × 38 | 160 × 124 × 48.8, up to 50.8 including adjusted screw heads |
| [Suncronizer](../cases/suncronizer/) | Open supply estimated at 104 × 57–58 × 26 | Supply bay 110 × 65 × 32, converter bay 50 × 30 × 20 including connectors | 164 × 116 × 39.8 |

## Delta ADP-300AF T mounting datums

The host is the A1419 iMac17,1, 27-inch Retina 5K (Late 2015). The parts listing associates Apple 661-03524 with Delta ADP-300AF T and Lite-On PA-1311-2A. The Delta layout is the design reference. Check the label before selecting this kit. [Apple](https://support.apple.com/en-gb/108054) · [Beetstech](https://beetstech.com/product/imac-27-inch-a1419-300w-power-supply-661-03524)

The 99 mm dimension is the vertical distance between mounting rows. The 3.4 mm underside gap is measured from the inner floor surface to the PCB support plane.

Coordinates use the upper-left PCB corner in plan view, with the A–B row at the top. X increases rightward and Y downward. Estimated centers in mm are A (12, 3), B (160, 3), C (5, 102) and D (158, 102), each with approximately ±2 mm uncertainty. Row separation is 99 mm vertically. The horizontal spans are 148 and 153 mm. Check the diagonal alignment as well as the spans. The holes are estimated at 3.5–4 mm in diameter with an outer ring of approximately 8 mm. The printed pads are 9 mm across.

At maximum modeled component height, 5 mm remains between the component envelope and the inner ceiling. The nominal 3.4 mm gap under the PCB must accommodate the actual solder projections. The 12.6 mm cable ports are on opposite ends. The clamp fit study covers round jackets 4–12 mm in diameter. The two clearances and clamp range describe geometry. Electrical insulation, heat dissipation and strain relief require physical assessment.

## Fit checks before printing

- **AURA S-60-12** retains the original metal housing. Measure the particular supply and check the terminal location. The decimals in the STEP bounding box describe model geometry rather than a manufacturing tolerance.
- **AURA Compact 160** uses supports and adjustable screws that contact solid housing metal. Its estimated 75–80 mm spacing between visible mounting holes was not used as a fixing datum. Check the uncertain 110 mm length including projections, the 13.7 mm allowance at the terminal end and the complete DC cable bend.
- **Suncronizer** reserves a volume for a converter that has yet to be selected. Check the connectors as well as its board. The 26 mm supply height has the greatest uncertainty. Board mounting points have yet to be defined for a physical assembly.

[Validation method](method.md) · [P1S print setup](printing.md)
