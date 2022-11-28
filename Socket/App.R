library(shiny)
library(shinyjs)
closeAllConnections()

# Connection to the socket
host <- "127.0.0.1"
port <- 6007
con <- make.socket(host, port)
writeLines(paste("-- Server --", "\n", "Host: ", host, "\n","Port: ", port))

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  useShinyjs(),
  actionButton("go", label = "Go!"),
  actionButton("stop", label = "Stop!"),
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
      
      # Output: Tabset w/ plot, summary, and table
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
  
  observeEvent(input$tabs, {
    
    print(paste("You clicked tab:", input$tabs))
    print(paste("The ID session is :", session$token))
    msg <<- paste0("[",Sys.time(), "] You clicked tab : ", input$tabs, " | Your session ID is : ", session$token)
    
    #Send data
    write.socket(con, msg)
    
    #Read the socket
    statusMsg = read.socket(con, loop=TRUE)
    print(statusMsg)
  }
  )
}

# Run the application 
shinyApp(ui=ui, server=server)