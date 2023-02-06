library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  textOutput('status'),
  uiOutput("image"),
  
  # Application title
  titlePanel("test"),
  
  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      sliderInput("bins",
                  "Number of bins:",
                  min = 1,
                  max = 50,
                  value = 30)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("distPlot"),
      htmlOutput("showfile"),
      
      # Création d'onglets nommés : plot, summary, et table
      tabsetPanel(id = "tabs",
                  tabPanel("Plot", plotOutput("ID1")),
                  tabPanel("Summary", verbatimTextOutput("ID2")),
                  tabPanel("Table", tableOutput("ID3"))
      )
    )
  )
)

# Define server logic required to draw a histogram
server <- function(input, output, session) {
  
  output$showfile <- renderUI({
    includeHTML("C:/Users/doure/rasa/index.html")
  })
  
  con <<- make.socket(host="localhost", port=5006, server=TRUE)
  
  observeEvent(input$tabs, {
    print(paste("You clicked tab:", input$tabs))
    print(paste("The ID session is :", session$token))
    msg <<- paste0("[",Sys.time(), "] You clicked tab : ", input$tabs, " | Your session ID is : ", session$token)
    
    #Send data
    #write.socket(con, msg)
    
    #Read the socket
    statusMsg = read.socket(con, loop=TRUE)
    print(statusMsg)
    
    var1 <- grepl("plot|Plot|PLOT", statusMsg)
    if (var1 == TRUE){
      updateTabsetPanel(session, "tabs", selected = "Plot")
      var1=FALSE}
    var2 <- grepl("summary|Summary|SUMMARY", statusMsg)
    if (var2 == TRUE){
      updateTabsetPanel(session, "tabs", selected = "Summary")
      var2=FALSE}
    var3 <- grepl("table|Table|TABLE", statusMsg)
    if (var3 == TRUE){
      updateTabsetPanel(session, "tabs", selected = "Table")
      var3=FALSE}
  }
  )
}
# Run the application 
shinyApp(ui=ui, server=server)