/**
 * TiLearn: desktop doc TOC with LangChain-style "On this page" heading.
 * Swizzled from @docusaurus/theme-classic theme/TOC.
 */

import React, { type ReactNode } from "react";
import clsx from "clsx";
import Translate from "@docusaurus/Translate";
import TOCItems from "@theme/TOCItems";
import type { Props } from "@theme/TOC";

import styles from "./styles.module.css";

const LINK_CLASS_NAME = "table-of-contents__link toc-highlight";
const LINK_ACTIVE_CLASS_NAME = "table-of-contents__link--active";

function OnThisPageIcon(): ReactNode {
  return (
    <svg
      className={styles.onThisPageIcon}
      width={16}
      height={16}
      viewBox="0 0 16 16"
      aria-hidden
    >
      <line
        x1="2"
        y1="4"
        x2="9"
        y2="4"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
      <line
        x1="2"
        y1="8"
        x2="14"
        y2="8"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
      <line
        x1="2"
        y1="12"
        x2="11"
        y2="12"
        stroke="currentColor"
        strokeWidth="1.5"
        strokeLinecap="round"
      />
    </svg>
  );
}

export default function TOC({ className, ...props }: Props): ReactNode {
  return (
    <div className={clsx(styles.tableOfContents, "thin-scrollbar", className)}>
      <div className={styles.onThisPageHeading}>
        <OnThisPageIcon />
        <Translate
          id="theme.TOC.onThisPageHeading"
          description="Heading shown above the in-page table of contents on documentation pages"
        >
          On this page
        </Translate>
      </div>
      <TOCItems
        {...props}
        linkClassName={LINK_CLASS_NAME}
        linkActiveClassName={LINK_ACTIVE_CLASS_NAME}
      />
    </div>
  );
}
