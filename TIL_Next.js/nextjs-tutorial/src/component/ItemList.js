import { Grid } from "semantic-ui-react"

export default function ItemList({ list }) {
  return (
    <div>
      <Grid columns={3}>
        <Grid.Row>
          {list.map((item) => (
            <Grid.Column>
              <img src={item.image_link} alt={item.name} />
            </Grid.Column>
          ))}
        </Grid.Row>
      </Grid>
    </div>
  )
}