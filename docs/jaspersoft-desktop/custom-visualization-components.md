# Custom visualization components

A **custom visualization component** draws what no element of the palette draws: a chart of a kind
of its own, a diagram, a map, anything a web page can show. It is a small JavaScript program; the
report gives it data and settings, and the engine prints the picture it draws, in the preview, in
PDF, in every export.

In Jaspersoft Desktop the AI assistant writes them for you: you describe what you want, it writes
the code, builds the component, looks at what it draws and corrects it. You do not need to know
JavaScript, though you can read and change everything it writes.

## Asking for one

In a folder workspace, with a report open, ask the assistant (see
[Working with the AI assistant](tutorial-ai.md)):

> Make a component that draws the sales of each country as a donut, and put it in the summary

The assistant:

1. writes the component, in a folder of the workspace, `/components/<name>`;
2. installs the libraries it needs (for example D3 or ECharts): this one it **asks** you first,
   since they are downloaded from the internet onto your computer;
3. **builds** it, and **draws** it once with sample data to see the result, correcting what does
   not look right;
4. **proposes** to add it to the report, with the data it reads from the report's dataset.

When you apply the proposal, the component is on the page as a **CVC** element. Run the preview to
see it with the report's data.

## What a component is made of

The folder `/components/<name>` holds:

| File | What it is |
| --- | --- |
| `component.json` | What the component is: its name, its settings and the data it takes. Jaspersoft Studio reads the same file. |
| `src/` | Its code. |
| `package.json` | The libraries it uses. |
| `dist/` | The built component: what the report loads. |

The explorer shows the folder with an icon of its own. You can open and edit any of the files in
the code editor; after a change, right-click the folder and choose **Build Component**, or ask the
assistant to build it.

## The component in a report

A **CVC** element of the palette runs a component. Select it on the page: its **Properties** list
the settings the component describes in `component.json` (colors, sizes, titles…), each with its
type and default, and the **data** it takes from the report: for each data set, the dataset it
reads and the expressions of its items.

Every report of the workspace can use the same component. Ask the assistant to change it ("make
the donut thinner", "add a legend") and every report that uses it changes with it.

## On JasperReports Server

On a JasperReports Server, the viewer loads a component's script and style sheet from the report
unit: they have to be resources of the unit. When you pick them from the server's repository for
the CVC element of a unit's report, Jaspersoft Desktop says so and offers to link them to the unit:
a link, not a copy, so every report shares one component. Building components needs a folder
workspace: build them there, then put their built files (`dist/`) on the server.

## When it does not draw

- **Build it again**: right-click the folder, **Build Component**. The assistant's build tells what
  failed.
- **Ask the assistant to test it**: it draws the component and sees what you see.
- **The data**: a component draws nothing when its data set is empty; check the dataset it reads,
  in the element's **Properties**.
