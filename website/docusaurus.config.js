// @ts-check

const config = {
  title: 'EventFlow',
  tagline: 'Bilheteira simples para eventos organizados do planeamento a porta',
  favicon: 'img/favicon.svg',

  url: 'https://brunobremert.github.io',
  baseUrl: '/LESTI2026-projeto1/',
  trailingSlash: false,
  organizationName: 'BrunoBremert',
  projectName: 'LESTI2026-projeto1',

  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: 'docs',
          editUrl: 'https://github.com/BrunoBremert/LESTI2026-projeto1/tree/main/website/',
        },
        blog: {
          showReadingTime: true,
          routeBasePath: 'novidades',
          blogTitle: 'Novidades EventFlow',
          blogDescription: 'Notas de progresso do projeto e evolucao do produto.',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    image: 'img/eventflow-social-card.svg',
    navbar: {
      title: 'EventFlow',
      logo: {
        alt: 'EventFlow logo',
        src: 'img/logo.svg',
      },
      items: [
        {to: '/', label: 'Inicio', position: 'left'},
        {to: '/docs/intro', label: 'Documentacao', position: 'left'},
        {to: '/docs/git-workflow', label: 'Git', position: 'left'},
        {to: '/novidades', label: 'Novidades', position: 'left'},
        {
          href: 'https://github.com/BrunoBremert/LESTI2026-projeto1',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Produto',
          items: [
            {label: 'Visao geral', to: '/docs/intro'},
            {label: 'Funcionalidades', to: '/docs/funcionalidades'},
            {label: 'Instalacao', to: '/docs/instalacao'},
          ],
        },
        {
          title: 'Projeto',
          items: [
            {label: 'Fluxo Git', to: '/docs/git-workflow'},
            {label: 'Markdown', to: '/docs/markdown-showcase'},
            {label: 'Novidades', to: '/novidades'},
          ],
        },
        {
          title: 'Codigo',
          items: [
            {
              label: 'Repositorio',
              href: 'https://github.com/BrunoBremert/LESTI2026-projeto1',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} EventFlow. Projeto academico LESTI.`,
    },
    prism: {
      theme: require('prism-react-renderer').themes.github,
      darkTheme: require('prism-react-renderer').themes.dracula,
    },
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },
  },
};

export default config;
