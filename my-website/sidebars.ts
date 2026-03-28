import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    "index",
    "getting-started/index",
    {
      type: "category",
      label: "User Guide",
      link: { type: "doc", id: "user-guide/index" },
      items: [
        "user-guide/index",
        "user-guide/single-machine/lateness/edd",
        "user-guide/single-machine/completion/wspt",
        "user-guide/illustrate",
      ],
    },
    "building-from-source/index",
    {
      type: "category",
      label: "API reference",
      link: { type: "doc", id: "api-reference/index" },
      items: ["api-reference/index", "api-reference/in-job/i-job"],
    },
    "news/index",
    "about",
  ],
};

export default sidebars;
