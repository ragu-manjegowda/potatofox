# potatofox
[![please don't upload to github](https://nogithub.codeberg.page/badge.svg)](https://nogithub.codeberg.page)

<div style="display: flex;">
<div style="flex: 1;">

a firefox and sidebery css theme.

> [!note]
> only linux is supported, macos and windows should work but may have
> issues.

## features

- collapsing vertical tabs using sidebery
- pop-up arc-like urlbar
- option to hide the navbar
- ability to remove borders around webpage for an ultra minimal experience
- general visual enhancements
- custom svg icons for some extensions
- support for vertical tabs on the left or right
- tons for blur and translucency

</div>

<div style="flex: 1;">
<img src="./media/screenshot0.png" width="100%" alt="firefox with custom css applied">
</div>
</div>

## screenshots

<div align="center">
<img src="./media/screenshot1.png" width="49%" alt="potatofox theme with sidebar collapsed">
<img src="./media/screenshot2.png" width="49%" alt="potatofox theme with navbar hidden and sidebar collapsed">
<img src="./media/screenshot3.png" width="32%" alt="potatofox theme with navbar and sidebar hidden while the urlbar is floating">
<img src="./media/screenshot4.png" width="32%" alt="potatofox theme with navbar and sidebar hidden">
<img src="./media/screenshot5.png" width="32%" alt="borderless potatofox theme with navbar and sidebar hidden">
</div>

## install instructions

extension:

- [sidebery](https://addons.mozilla.org/en-us/firefox/addon/sidebery)
- [userchrome toggle extended](https://addons.mozilla.org/en-us/firefox/addon/userchrome-toggle-extended)
- [firefox color](https://addons.mozilla.org/en-us/firefox/addon/firefox-color) (optional)

open the [releases tab](https://codeberg.org/da157/potatofox/releases) and download the correct release for your version of firefox
(urlbar > about:support > application basics > version). then copy the chrome directory
and user.js file into your firefox profiles directory
(about:support > application basics > profile directory), then restart firefox.

<details><summary>advanced (cli) install (macos/linux)</summary>

#### using git

```bash
git clone https://codeberg.org/da157/potatofox.git
cd potatofox
ln -sr user.js chrome ~/.mozilla/firefox/<profile> # linux
cp -r user.js chrome ~/library/application support/firefox/profiles/<profile> # macos
```

#### using [nyoom](https://github.com/ryanccn/nyoom)

```bash
nyoom profile <profile-dir>
nyoom add codeberg:da157/potatofox
nyoom switch potatofox
```

> [!note]
> make sure to install the required extensions.

</details>

## post install

- import sidebery config (sidebery settings > help > import addon data)
- import firefox color [theme](https://color.firefox.com/?theme=xqaaaajlbaaaaaaaaabbqyhm849scicxcucpx38okricm6da8pg5gi-drbs7fiefluzdswxwyuhmskhz2pprk_lvzgtf44fp7vnvxujpkkmjvowqsihdk22u1zg2egdmynmx_0okj3h6sapxy3iyq4dsjp5wxsjae_-1mtfwgrdmsdoscoijqwjmgbopoyezc-rlltczgrdec_ybcl7rnqk6talv9hrkp2vkgfddbs2rhmpkmp4ntmrarv5vn93xej36dj4pjls8lr2xw5gejnc2ynldh0ltcv_docqu1k6c8gqp4wdfykereqqmlzlot6aycj_r86a_oadsjnzxh2qs7opwswemt1d06l1xq2dyeabxh9ztifsky5cury2m6x_epyax9nybjgeiensjyqdtye4ssm-vvysrkhhtfwcmzpvjidgaiaftrbal5lonnlhf9s7kku6o9y9kvvr2zcff2v6tyspyu0plozefn9_9cznq4yy1eac1ciaw-_h5rghx3pdhdfrzk6gsi1tw-illtdydu8f1rvkzrjnxgle0yzdpy6-qm0ihykgrx6ulvurtm_5nv9wkmf0ueizsabe_abxh8cr_0f-fxa) (optional)
- about:addons (url) > userchrome toggle extended preferences >
  general settings > allow multiple styles to be active together, apply changes

> [!warning]
> some websites with a white background will have an incorrect background, this
> can be fixed by using [dark reader](https://addons.mozilla.org/firefox/addon/darkreader/)
> or by removing `browser.tabs.allow_transparent_browser` from `user.js`

> [!tip]
> on linux there may be extra padding before/after the window controls, this can
> be fixed by changing line 36-38 in `chrome/vars.css`

> [!tip]
> if fingerprinting is a concern for you, i recommend enabling `uc.tweak.no-custom-icons`
> and removing `svg.context-properties.content.enabled` from `user.js`

### recommended userchrome toggle extended settings

<div align="center">
<img src="./media/uc_toggle_settings.png" width="600" alt="userchrome toggle settings">
</div>

### about:config tweaks

| setting                      | description                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| uc.tweak.borderless          | removes margins around the webpage                                                                                                   |
| uc.tweak.borderless.no-round | don't round corners of browser contents when in borderless mode
| uc.tweak.no-custom-icons     | don't apply custom monochrome icons for some extensions                                                                              |
| uc.tweak.no-window-controls  | removes window controls                                                                                                              |
| uc.tweak.no-panel-hint       | hide the small bars showing location of hidden panels                                                                                |
| uc.tweak.no-animations       | disable animations added by this theme                                                                                               |
| uc.tweak.urlbar.not-floating | urlbar no longer floats in center of window when focused                                                                             |
| uc.tweak.findbar.bottom      | moves findbar to bottom of webpage (causes it to not be visible when devtools are active on bottom)                                  |
| sidebar.position_start       | controls if the sidebar is on the left or right                                                                                      |
| uc.tweak.sidebar.short       | makes sidebar shorter when hovering (140px)                                                                                          |
| uc.tweak.sidebar.wide        | makes sidebar wider when hovering (200px)                                                                                            |
| uc.tweak.sidebar.header      | show sidebar header                                                                                                                  |
| uc.tweak.sidebery.big-pinned | pinned tabs look like buttons, like arc's pinned tabs (make sure to set sidebery settings > tabs > pinned tabs > show titles is off) |
| uc.tweak.sidebery.top-navbar | move sidebery's navbar to the top of the sidebar                                                                                     |
| uc.tweak.no-blur             | remove blur and translucency from background of sidebery, navbar, urlbar, etc                                                                              |
| uc.tweak.translucency        | experimental translucent window background                                                                                           |

### advanced configuration

the variables used by the theme are in `vars.css` and `userchrome.css` (colors). if
you would like to ensure there aren't git conflicts you can add a `overrides.css`
file in the `chrome` directory and override the variables from `vars.css` in there (using
`!important;` is necessary). keep in mind the theme defaults to using `uidensity="compact"`,
so you will want to change the variables inside there.

## inspo

[kikaraage](https://github.com/kikaraage/arcwtf) - arcwtf

[shina-sg](https://github.com/shina-sg/shina-fox) - shina-fox

[artsyfriedchicken](https://github.com/artsyfriedchicken/edgyarc-fr) - edgyarc-fr

[naezer](https://github.com/naezr/shyfox) - shyfox

## mirrors

currently potatofox is available on [codeberg](https://codeberg.org/da157/potatofox) (main)
and [tangled](https://tangled.org/da157.id/potatofox) and [git.gay](https://git.gay/awwpotato/potatofox) (mirrors)

## license

the source code of this project is subject to the terms of the [mplv2.0](https://www.mozilla.org/en-us/mpl/2.0/) license.
all documentation and images included as part of this readme are licensed under [cc by-sa](https://creativecommons.org/licenses/by-sa/4.0/).
