import { Grid } from "semantic-ui-react"

export default function ItemList({ list }) {
  return (
    <div>
      <Grid columns={3}>
        <Grid.Row>
          {list.map((item) => (
            <Grid.Column>
              <img src={item.image_link} alt={item.name} />
              <strong>{item.name}</strong>
              <span>
                {item.category} {item.product_type}
              </span>
              <strong>${item.price}</strong>
            </Grid.Column>
          ))}
        </Grid.Row>
      </Grid>
    </div>
  )
}