import clsx from 'clsx';
import Heading from '@theme/Heading';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import styles from './index.module.css';

const features = [
  {
    title: 'Eventos com setores',
    description:
      'Crie zonas como VIP, plateia ou geral, defina capacidade e acompanhe vagas em tempo real.',
  },
  {
    title: 'Compra e validacao',
    description:
      'A simulacao de compra gera um codigo de entrada e a equipa de staff valida bilhetes na porta.',
  },
  {
    title: 'Dashboard operacional',
    description:
      'Receita, ocupacao, check-ins e eventos populares ficam reunidos numa leitura simples.',
  },
];

const stats = [
  ['3', 'perfis de utilizacao'],
  ['100%', 'dados em JSON'],
  ['9+', 'operacoes no menu'],
];

function Hero() {
  return (
    <header className={styles.hero}>
      <div className={styles.heroInner}>
        <div className={styles.heroCopy}>
          <span className={styles.kicker}>Sistema de bilheteira academico</span>
          <Heading as="h1" className={styles.heroTitle}>
            EventFlow
          </Heading>
          <p className={styles.heroSubtitle}>
            Uma aplicacao para organizar eventos, vender bilhetes por setor,
            validar entradas e perceber a ocupacao sem complicar a operacao.
          </p>
          <div className={styles.heroActions}>
            <Link className="button button--primary button--lg" to="/docs/intro">
              Ver documentacao
            </Link>
            <Link className="button button--secondary button--lg" to="/docs/git-workflow">
              Fluxo Git
            </Link>
          </div>
        </div>
        <div className={styles.productPanel} aria-label="Resumo visual do produto">
          <div className={styles.panelHeader}>
            <span>Dashboard</span>
            <strong>Hoje</strong>
          </div>
          <div className={styles.metricGrid}>
            <div>
              <span>Receita</span>
              <strong>2 430 EUR</strong>
            </div>
            <div>
              <span>Check-ins</span>
              <strong>78%</strong>
            </div>
          </div>
          <div className={styles.eventList}>
            <div>
              <strong>Tech Summit</strong>
              <span>VIP 42/60</span>
            </div>
            <div>
              <strong>Noite Academica</strong>
              <span>Geral 180/220</span>
            </div>
            <div>
              <strong>Mostra Cultural</strong>
              <span>Plateia 96/120</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

function FeatureCard({title, description}) {
  return (
    <article className={styles.featureCard}>
      <Heading as="h3">{title}</Heading>
      <p>{description}</p>
    </article>
  );
}

export default function Home() {
  return (
    <Layout
      title="EventFlow"
      description="Site Docusaurus para publicitar a aplicacao EventFlow">
      <Hero />
      <main>
        <section className={styles.statsBand}>
          {stats.map(([value, label]) => (
            <div key={label} className={styles.stat}>
              <strong>{value}</strong>
              <span>{label}</span>
            </div>
          ))}
        </section>

        <section className={styles.section}>
          <div className="container">
            <div className={styles.sectionHeading}>
              <span className={styles.kicker}>Da organizacao a entrada</span>
              <Heading as="h2">Tudo o que um pequeno evento precisa</Heading>
            </div>
            <div className={clsx('row', styles.featureGrid)}>
              {features.map((props) => (
                <div className="col col--4" key={props.title}>
                  <FeatureCard {...props} />
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className={styles.workflowBand}>
          <div className="container">
            <div className={styles.workflow}>
              <div>
                <span className={styles.kicker}>Workflow</span>
                <Heading as="h2">Um produto com historia de desenvolvimento</Heading>
                <p>
                  O repositorio inclui ramos de funcionalidades, merges e
                  commits organizados. O site acrescenta a camada de divulgacao
                  pedida no TP3 sem apagar a evolucao anterior da aplicacao.
                </p>
              </div>
              <Link className="button button--outline button--lg" to="/docs/git-workflow">
                Consultar evidencias
              </Link>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
