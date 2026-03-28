import Link from "@docusaurus/Link";
import useBaseUrl from "@docusaurus/useBaseUrl";
import type { ReactNode } from "react";
import { DOC_CARDS, GITHUB_URL, PYPI_URL } from "./links";
import styles from "./styles.module.css";

export default function TiLearnHomepage(): ReactNode {
  const githubImg = useBaseUrl("/img/github-mark.png");
  const pypiImg = useBaseUrl("/img/pypi.png");

  return (
    <div className={styles.root}>
      <header className={styles.hero}>
        <div className={styles.heroGlow} aria-hidden />
        <div className={styles.heroInner}>
          <h1 className={styles.title}>TiLearn</h1>
          <p className={styles.tagline}>Optimize your time with AI</p>
          <p className={styles.lead}>
            Open-source tools for <strong>time management</strong> and{" "}
            <strong>scheduling</strong>. TiLearn combines scheduling ideas from operations
            research with a practical Python API so you can organize work, explore
            single-machine models, and ship faster—whether you are learning, building, or
            contributing.
          </p>
          <div className={styles.ctaRow}>
            <Link className={styles.btnPrimary} to="/getting-started">
              Get started
            </Link>
            <a
              className={styles.btnOutline}
              href={GITHUB_URL}
              target="_blank"
              rel="noopener noreferrer"
            >
              <img className={styles.btnIcon} src={githubImg} alt="" aria-hidden />
              GitHub
            </a>
            <a
              className={styles.btnOutline}
              href={PYPI_URL}
              target="_blank"
              rel="noopener noreferrer"
            >
              <img className={styles.btnIcon} src={pypiImg} alt="" aria-hidden />
              PyPI
            </a>
          </div>
          <Link className={styles.releaseLink} to="/news">
            TiLearn 0.0.10 released — see what&apos;s new
          </Link>
        </div>
      </header>

      <section className={styles.section} aria-labelledby="docs-heading">
        <h2 id="docs-heading" className={styles.sectionTitle}>
          Documentation
        </h2>
        <div className={styles.grid}>
          {DOC_CARDS.map((card) => (
            <Link key={card.to} className={styles.card} to={card.to}>
              <h3 className={styles.cardTitle}>{card.title}</h3>
              <p className={styles.cardDesc}>{card.description}</p>
              <span className={styles.cardArrow}>Read more →</span>
            </Link>
          ))}
        </div>
      </section>

      <p className={styles.footer}>
        Questions, ideas, or contributions are welcome. Reach out on{" "}
        <a href={GITHUB_URL} target="_blank" rel="noopener noreferrer">
          GitHub
        </a>{" "}
        or connect via the links in the site footer.
      </p>
    </div>
  );
}
