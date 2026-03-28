import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

const config: Config = {
  title: "TiLearn",
  tagline: "Optimize your time with AI",
  favicon: "img/tilearn.png",

  future: {
    v4: true,
  },

  url: "https://bancie.github.io",
  baseUrl: "/TiLearn/",

  organizationName: "Bancie",
  projectName: "TiLearn",

  onBrokenLinks: "warn",

  markdown: {
    format: "detect",
  },

  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  stylesheets: [
    {
      href: "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css",
      type: "text/css",
      crossorigin: "anonymous",
    },
  ],

  presets: [
    [
      "classic",
      {
        docs: {
          routeBasePath: "/",
          sidebarPath: "./sidebars.ts",
          editUrl:
            "https://github.com/Bancie/TiLearn/tree/main/my-website/docs/",
          remarkPlugins: [[remarkMath, { singleDollarTextMath: true }]],
          rehypePlugins: [rehypeKatex],
        },
        blog: false,
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: "img/tilearn2.png",
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: "TiLearn",
      logo: {
        alt: "TiLearn",
        src: "img/tilearn2.png",
      },
      items: [
        {
          type: "doc",
          docId: "index",
          position: "left",
          label: "Home",
        },
        {
          type: "doc",
          docId: "getting-started/index",
          position: "left",
          label: "Getting started",
        },
        {
          type: "doc",
          docId: "user-guide/index",
          position: "left",
          label: "User Guide",
        },
        {
          type: "doc",
          docId: "building-from-source/index",
          position: "left",
          label: "Building from source",
        },
        {
          type: "doc",
          docId: "api-reference/index",
          position: "left",
          label: "API reference",
        },
        {
          type: "doc",
          docId: "news/index",
          position: "left",
          label: "News",
        },
        {
          type: "doc",
          docId: "about",
          position: "left",
          label: "About",
        },
        {
          href: "https://github.com/Bancie/TiLearn",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            { label: "Getting started", to: "/getting-started" },
            { label: "User Guide", to: "/user-guide" },
            { label: "API reference", to: "/api-reference" },
          ],
        },
        {
          title: "Community",
          items: [
            {
              label: "Facebook",
              href: "https://web.facebook.com/ngchibangg",
            },
            {
              label: "Instagram",
              href: "https://www.instagram.com/bancie.007/",
            },
            { label: "GitHub", href: "https://github.com/Bancie/TiLearn" },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} <a href="https://web.facebook.com/ngchibangg" target="_blank" rel="noopener noreferrer">Bancie Nguyen</a>. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
