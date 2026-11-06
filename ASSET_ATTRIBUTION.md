# Asset attribution

Reviewed October 31, 2026. This page separates original case-study material,
simulator imagery, and third-party content rendered by the application. It does
not certify the complete upstream provenance of every source asset.

## November 6 public gallery scope

The current gallery contains seven native PNGs retained from the original
nine-image capture pass. The earlier body-model rendering and its associated
older detail image are omitted while their wider-distribution scope is reviewed.
The retained readiness interface shows its partial simulated-input qualification.

The historical source credits below remain applicable to the material they
describe. Omission does not certify all upstream rights, remove older commits,
or change any third-party license. No private native source, raw model, texture
or anatomical source data is added by this revision.

## Simulator images

The case study uses application captures from a dedicated simulator scenario
with synthetic demo/test records. The final image list, capture dates, and
observed scenes are maintained in the [screenshot record](screenshots/README.md).
Earlier public images dated August 9, 2026, are historical references and do not
prove later application changes.

The app interface and third-party material visible in an image retain their
respective rights. The general [case-study usage statement](CASE_STUDY_USAGE.md)
does not override third-party licenses.

## Derived body-model material

The current application's model notice describes a combined asset using a
MakeHuman body surface and region borders/normal mapping derived from
Z-Anatomy and BodyParts3D. The raw model, texture, anatomical source data, and
muscle map are not distributed in this case-study repository.

Credit carried from the model notice:

- **Z-Anatomy - The libre 3D atlas of anatomy - CC-BY-SA 4.0**.
  [Source project](https://github.com/Z-Anatomy/Models-of-human-anatomy).
  Gauthier Kervyn: design, 3D, and anatomy; Marcin Zielinski: Blender add-on;
  Lluis Vinent: Unity application.
- **BodyParts3D - The Database Center for Life Science - CC-BY-SA 2.1 Japan**.
  This is the historical credit retained by Z-Anatomy and the app's model
  notice for its source lineage. Original model: Kousaku Okubo.
  [Source database and downloads](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html).
- **MakeHuman (CC0)**. The application notice identifies the base mesh, morph
  targets, and rig weights as CC0 asset data.
  [Source project](https://github.com/makehumancommunity/makehuman) and
  [asset-license explanation](https://github.com/makehumancommunity/makehuman/blob/master/LICENSE.md).

The application's combined model, texture, and muscle map are identified by its
notice as [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Associated rendered body-model material is credited here under that notice.
The license link describes attribution, change notices, and ShareAlike terms;
these are not replaced by SetFlow's case-study copyright statement.

The current BodyParts3D provider page, updated February 27, 2025, separately
lists CC Attribution 4.0 and requests this credit: “BodyParts3D, © The Database
Center for Life Science licensed under CC Attribution 4.0 International.”
[Current provider license notice](https://dbarchive.biosciencedbc.jp/en/bodyparts3d/lic.html).
This newer provider statement does not change the historical lineage credit
requested by Z-Anatomy or relicense the app's combined derivative in this page.

### Changes described by the application notice

The MakeHuman surface was morphed, posed, and aligned to the reference figure.
Its skin was divided into application muscle regions, with borders derived
from underlying Z-Anatomy muscles. A subtle normal map was baked from a
smoothed muscle/tendon envelope. Later application work revised region mapping
and the rendered appearance.

The notice identifies the muscular source collection and states that the
non-commercial inner-ear and kidney assets were excluded. This page records
that declared build scope; it is not an independent audit of the source build.
No endorsement by the source projects or their authors is implied.

## Conceptual diagrams

The two SVG diagrams in `media/` are case-study illustrations of the product
workflow and report boundary. They are labeled conceptual and are not app
screenshots, anatomy data, or a complete implementation diagram.

## Scope of the usage statement

The application code and other original SetFlow material are separate from the
body-model license. This repository does not grant access to the private code
or apply a blanket SetFlow ownership claim to third-party material. Consult the
linked source and license notices for those materials.
