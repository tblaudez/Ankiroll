<h2 align="center">Anki with a chance of Rickroll</h2>

> Never gonna give you up... but maybe your flashcards will !

An add-on for the spaced-repetition flashcard app [Anki](https://apps.ankiweb.net/) that will bring a fun twist to your Anki reviews by randomly displaying a Rickroll before each answer is shown.

<p align="center"><img src="screenshots/rick.gif" height=500></p>

### Acknowledgments

The code architecture of **Ankiroll** is heavily inspired by [Ankitty](https://github.com/marvinruder/ankitty) by marvinruder, which itself is a fork of [Puppy Reinforcement](https://github.com/glutanimate/puppy-reinforcement) by glutanimate.

Big thanks to these awesome developers for their work! Without them, Ankiroll wouldn’t have had such a solid foundation to deliver unexpected Rickrolls to unsuspecting learners !

Never gonna give you up... but definitely gonna give you credit! 🚀

### Table of Contents <!-- omit in toc -->

<!-- MarkdownTOC levels="1,2,3" -->

- [Installation](#installation)
- [Building](#building)
- [Acknowledgments](#acknowledgments)
- [License and Credits](#license-and-credits)

<!-- /MarkdownTOC -->

### Installation

#### AnkiWeb <!-- omit in toc -->

The easiest way to install Ankitty is through [AnkiWeb](https://ankiweb.net/shared/info/597778000).

#### Manual installation <!-- omit in toc -->

1. Download the latest `.ankiaddon` file from the [releases tab](https://github.com/tblaudez/Ankiroll/releases) (you might need to click on *Assets* below the description to reveal the download links)
2. Open the folder where your downloads are located and double-click on the downloaded `.ankiaddon` file.
3. Follow the installation prompt and restart Anki if it asks you to

<details>

<summary><i>Alternate option</i></summary>

1. Download the latest `.ankiaddon` package from the [releases tab](https://github.com/tblaudez/Ankiroll/releases) (you might need to click on *Assets* below the description to reveal the download links)
2. From Anki's main window, head to *Tools* → *Add-ons*
3. Drag-and-drop the `.ankiaddon` package onto the add-ons list
4. Restart Anki

</details>

### Building

With [Anki add-on builder](https://github.com/glutanimate/anki-addon-builder/) installed:

    git clone https://github.com/tblaudez/Ankiroll.git
    cd Ankiroll
    aab build

For more information on the build process please refer to [`aab`'s documentation](https://github.com/glutanimate/anki-addon-builder/#usage).


### License and Credits

Ankitty is free and open-source software. The add-on code that runs within Anki is released under the GNU AGPLv3 license, extended by a number of additional terms. For more information please see the [LICENSE](https://github.com/marvinruder/ankitty/blob/main/LICENSE) file that accompanied this program.

Please note that this program uses the [Libaddon](https://github.com/glutanimate/anki-libaddon/) library which comes with [its own additional terms extending the GNU AGPLv3 license](https://github.com/marvinruder/ankitty/blob/main/src/puppy_reinforcement/libaddon/LICENSE). You may only copy, distribute, or modify the present compilation of this program with Libaddon under the combined licensing terms specified by both licenses.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY.

