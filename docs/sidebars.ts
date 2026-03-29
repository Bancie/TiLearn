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
        "user-guide/single-machine/completion/wspt",
        "user-guide/single-machine/lateness/edd",
        "user-guide/illustrate",
      ],
    },
    "building-from-source/index",
    {
      type: "category",
      label: "API reference",
      link: { type: "doc", id: "api-reference/index" },
      items: [
        {
          type: "category",
          label: "Modules",
          items: [
            "api-reference/modules/sorting",
            "api-reference/modules/basis",
            "api-reference/modules/data-io",
            "api-reference/modules/joblist",
          ],
        },
        {
          type: "category",
          label: "Migration",
          items: ["api-reference/in-job/i-job"],
        },
      ],
    },
    "news/index",
    "about",
  ],
};

export default sidebars;
